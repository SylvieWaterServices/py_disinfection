"""Main module."""

import math
from enum import Enum
from pydantic import BaseModel, Field, field_validator

from py_disinfection.estimation import (
    conservative_giardia_ct,
    interpolate_giardia_ct,
    regression_giardia_ct,
    conservative_viruses_ct,
    conservative_giardia_chlorine_dioxide_ct,
    conservative_viruses_chlorine_dioxide_ct,
    conservative_giardia_chloramines_ct,
    conservative_viruses_chloramines_ct,
)


class DisinfectantAgent(Enum):
    FREE_CHLORINE = "free_chlorine"
    CHLORINE_DIOXIDE = "chlorine_dioxide"
    CHLORAMINES = "chloramines"


class DisinfectionTarget(Enum):
    VIRUSES = "viruses"
    GIARDIA = "giardia"


class CTReqEstimator(Enum):
    CONSERVATIVE = "conservative"
    INTERPOLATION = "interpolation"
    REGRESSION = "regression"


DEFAULT_DISINFECTION_AGENT = DisinfectantAgent.FREE_CHLORINE
DEFAULT_CTREQ_ESTIMATOR = CTReqEstimator.CONSERVATIVE
DEFAULT_BAFFLING_FACTOR = 0.3
DEFAULT_PEAK_HOURLY_FLOW_GALLONS_PER_MINUTE = 10
DEFAULT_TEMPERATURE_CELSIUS = 20
DEFAULT_PH = 7
DEFAULT_CONCENTRATION_MG_PER_LITER = 1.0


class DisinfectionSegmentOptions(BaseModel):
    volume_gallons: float = Field(..., gt=0, description="Volume of water in gallons")
    temperature_celsius: float = Field(
        ..., ge=0, le=50, description="Water temperature in Celsius"
    )
    ph: float = Field(..., ge=6, le=9, description="pH level (6-9)")
    concentration_mg_per_liter: float = Field(
        ..., gt=0, description="Disinfectant concentration in mg/L"
    )
    baffling_factor: float = Field(
        ..., ge=0.1, le=1.0, description="Baffling factor (0.1 - 1.0)"
    )
    peak_hourly_flow_gallons_per_minute: float = Field(
        ..., gt=0, description="Peak flow rate in gallons per minute"
    )
    agent: DisinfectantAgent = Field(..., description="Disinfectant agent")
    ctreq_estimator: CTReqEstimator = Field(..., description="Estimation method")

    def __json__(self):
        return {
            "agent": self.agent.name,
            "volume_gallons": self.volume_gallons,
            "temperature_celsius": self.temperature_celsius,
            "ph": self.ph,
            "concentration_mg_per_liter": self.concentration_mg_per_liter,
            "peak_hourly_flow_gallons_per_minute": self.peak_hourly_flow_gallons_per_minute,
            "ctreq_estimator": self.ctreq_estimator.name,
            "baffling_factor": self.baffling_factor,
        }


class DisinfectionSegment:
    def __init__(self, options: DisinfectionSegmentOptions):
        self.options = options

    def __str__(self):
        return (
            f"DisinfectionSegment(agent={self.options.agent}, volume_gallons={self.options.volume_gallons}, "
            f"temperature_celsius={self.options.temperature_celsius}, ph={self.options.ph}, "
            f"concentration_mg_per_liter={self.options.concentration_mg_per_liter}, baffling_factor={self.options.baffling_factor}, "
            f"peak_hourly_flow_gallons_per_minute={self.options.peak_hourly_flow_gallons_per_minute}, estimator={self.options.ctreq_estimator})"
        )

    def __repr__(self):
        return self.__str__()

    def calculate_tdt(self):
        return (
            self.options.volume_gallons
            / self.options.peak_hourly_flow_gallons_per_minute
        )

    def calculate_contact_time(self):
        return self.calculate_tdt() * self.options.baffling_factor

    def calculate_ct(
        self,
    ):
        return self.calculate_contact_time() * self.options.concentration_mg_per_liter

    def required_ct(self, target: DisinfectionTarget):
        if target == DisinfectionTarget.GIARDIA:
            return self._required_ct_giardia()
        elif target == DisinfectionTarget.VIRUSES:
            return self._required_ct_viruses()
        raise InvalidTargetError(f"Invalid disinfection target: {target}")

    def _required_ct_giardia(self):
        if self.options.agent == DisinfectantAgent.FREE_CHLORINE:
            return self._required_ct_giardia_free_chlorine()
        elif self.options.agent == DisinfectantAgent.CHLORINE_DIOXIDE:
            return self._required_ct_giardia_chlorine_dioxide()
        elif self.options.agent == DisinfectantAgent.CHLORAMINES:
            return self._required_ct_giardia_chloramines()
        raise InvalidAgentError(f"Invalid disinfectant agent: {self.options.agent}")

    def _required_ct_viruses(self):
        if self.options.agent == DisinfectantAgent.FREE_CHLORINE:
            return self._required_ct_viruses_free_chlorine()
        elif self.options.agent == DisinfectantAgent.CHLORINE_DIOXIDE:
            return self._required_ct_viruses_chlorine_dioxide()
        elif self.options.agent == DisinfectantAgent.CHLORAMINES:
            return self._required_ct_viruses_chloramines()
        raise InvalidAgentError(f"Invalid disinfectant agent: {self.options.agent}")

    def _roundDownToNearest(self, x, base=5):
        return base * math.floor(x / base)

    def _roundUpToNearest(self, x, base=5):
        return base * math.ceil(x / base)

    def _required_ct_giardia_free_chlorine(self):
        if self.options.ctreq_estimator == CTReqEstimator.CONSERVATIVE:
            return conservative_giardia_ct(
                self.options.temperature_celsius,
                self.options.ph,
                self.options.concentration_mg_per_liter,
            )
        elif self.options.ctreq_estimator == CTReqEstimator.INTERPOLATION:
            return interpolate_giardia_ct(
                self.options.temperature_celsius,
                self.options.ph,
                self.options.concentration_mg_per_liter,
            )
        elif self.options.ctreq_estimator == CTReqEstimator.REGRESSION:
            return regression_giardia_ct(
                self.options.temperature_celsius,
                self.options.ph,
                self.options.concentration_mg_per_liter,
            )

    def _required_ct_giardia_chlorine_dioxide(self):
        if self.options.ctreq_estimator == CTReqEstimator.CONSERVATIVE:
            return conservative_giardia_chlorine_dioxide_ct(
                self.options.temperature_celsius
            )
        raise InvalidEstimatorError(
            f"{self.options.ctreq_estimator.name} not supported for giardia and chlorine dioxide"
        )

    def _required_ct_giardia_chloramines(self):
        if self.options.ctreq_estimator == CTReqEstimator.CONSERVATIVE:
            return conservative_giardia_chloramines_ct(self.options.temperature_celsius)
        raise InvalidEstimatorError(
            f"{self.options.ctreq_estimator.name} not supported for giardia and chloramines"
        )

    def _required_ct_viruses_free_chlorine(self):
        if self.options.ctreq_estimator == CTReqEstimator.CONSERVATIVE:
            return conservative_viruses_ct(
                self.options.temperature_celsius,
                self.options.ph,
            )
        raise InvalidEstimatorError(
            f"{self.options.ctreq_estimator.name} not supported for viruses and free chlorine"
        )

    def _required_ct_viruses_chlorine_dioxide(self):
        if self.options.ctreq_estimator == CTReqEstimator.CONSERVATIVE:
            return conservative_viruses_chlorine_dioxide_ct(
                self.options.temperature_celsius,
            )
        raise InvalidEstimatorError(
            f"{self.options.ctreq_estimator.name} not supported for viruses and chlorine dioxide"
        )

    def _required_ct_viruses_chloramines(self):
        if self.options.ctreq_estimator == CTReqEstimator.CONSERVATIVE:
            return conservative_viruses_chloramines_ct(
                self.options.temperature_celsius,
            )
        raise InvalidEstimatorError(
            f"{self.options.ctreq_estimator.name} not supported for viruses and chloramines"
        )

    def calculate_log_inactivation_ratio(self, target: DisinfectionTarget):
        required_ct = self.required_ct(target)
        if required_ct == 0:
            return math.inf
        return self.calculate_ct() / self.required_ct(target)

    def calculate_log_inactivation(self, target: DisinfectionTarget):
        if target == DisinfectionTarget.GIARDIA:
            return 3 * self.calculate_log_inactivation_ratio(target)
        elif target == DisinfectionTarget.VIRUSES:
            return 4 * self.calculate_log_inactivation_ratio(target)
        raise InvalidTargetError(f"Invalid disinfection target: {target}")

        return 1 - self.calculate_inactivation_ratio(
            concentration_mg_per_liter, target, agent
        )

    def analyze(self):
        results = {}
        results["tdt"] = self.calculate_tdt()
        results["contact_time"] = self.calculate_contact_time()
        for target in DisinfectionTarget:
            name = target.name.lower()
            results[f"{name}_required_ct"] = self.required_ct(target)
            results[f"{name}_calculated_ct"] = self.calculate_ct()
            results[f"{name}_ct_ratio"] = self.calculate_log_inactivation_ratio(target)
            results[f"{name}_log_inactivation"] = self.calculate_log_inactivation(
                target
            )
        return results


class NoTableEntryError(Exception):
    pass


class InvalidTargetError(Exception):
    pass


class InvalidAgentError(Exception):
    pass


class InvalidEstimatorError(Exception):
    pass
