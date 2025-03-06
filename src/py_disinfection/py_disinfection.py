"""Main module."""

import math
import json
from enum import Enum
from py_disinfection.estimation import conservative_ct, interpolate_ct, regression_ct


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


class DisinfectionSegmentOptions:
    agent: DisinfectantAgent
    ctreq_estimator: CTReqEstimator
    volume_gallons: float
    temperature_celsius: float
    ph: float
    concentration_mg_per_liter: float
    baffling_factor: float
    peak_hourly_flow_gallons_per_minute: float

    def __init__(
        self,
        volume_gallons,
        agent=DEFAULT_DISINFECTION_AGENT,
        temperature_celsius=DEFAULT_TEMPERATURE_CELSIUS,
        ph=DEFAULT_PH,
        concentration_mg_per_liter=DEFAULT_CONCENTRATION_MG_PER_LITER,
        peak_hourly_flow_gallons_per_minute=DEFAULT_PEAK_HOURLY_FLOW_GALLONS_PER_MINUTE,
        ctreq_estimator=DEFAULT_CTREQ_ESTIMATOR,
        baffling_factor=DEFAULT_BAFFLING_FACTOR,
    ):
        self.agent = agent
        self.volume_gallons = volume_gallons
        self.temperature_celsius = temperature_celsius
        self.ph = ph
        self.concentration_mg_per_liter = concentration_mg_per_liter
        self.peak_hourly_flow_gallons_per_minute = peak_hourly_flow_gallons_per_minute
        self.ctreq_estimator = ctreq_estimator
        self.baffling_factor = baffling_factor


class DisinfectionSegment:
    def __init__(self, options: DisinfectionSegmentOptions):
        self.options = options

    def __str__(self):
        return f"DisinfectionSegment(agent={self.options.agent}, volume_gallons={self.options.volume_gallons}, default_temperature_celsius={self.options.default_temperature_celsius}, default_ph={self.options.default_ph}, default_concentration_mg_per_liter={self.options.default_concentration_mg_per_liter}, baffling_factor={self.options.baffling_factor}, default_theoretical_detention_time_minutes={self.options.default_theoretical_detention_time_minutes}, peak_hourly_flow_gallons_per_minute={self.options.peak_hourly_flow_gallons_per_minute})"

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

    def _required_ct_giardia(self):
        if self.options.agent == DisinfectantAgent.FREE_CHLORINE:
            return self._required_ct_giardia_free_chlorine()
        elif self.options.agent == DisinfectantAgent.CHLORINE_DIOXIDE:
            return self._required_ct_giardia_chlorine_dioxide()
        elif self.options.agent == DisinfectantAgent.CHLORAMINES:
            return self._required_ct_giardia_chloramines()
        return None

    def _required_ct_viruses(self):
        if self.options.agent == DisinfectantAgent.FREE_CHLORINE:
            return self._required_ct_viruses_free_chlorine()
        elif self.options.agent == DisinfectantAgent.CHLORINE_DIOXIDE:
            return self._required_ct_viruses_chlorine_dioxide()
        elif self.options.agent == DisinfectantAgent.CHLORAMINES:
            return self._required_ct_viruses_chloramines()
        return None

    def _roundDownToNearest(self, x, base=5):
        return base * math.floor(x / base)

    def _roundUpToNearest(self, x, base=5):
        return base * math.ceil(x / base)

    def _required_ct_giardia_free_chlorine(self):
        if self.options.ctreq_estimator == CTReqEstimator.CONSERVATIVE:
            return conservative_ct(
                self.options.temperature_celsius,
                self.options.ph,
                self.options.concentration_mg_per_liter,
            )
        elif self.options.ctreq_estimator == CTReqEstimator.INTERPOLATION:
            return interpolate_ct(
                self.options.temperature_celsius,
                self.options.ph,
                self.options.concentration_mg_per_liter,
            )
        elif self.options.ctreq_estimator == CTReqEstimator.REGRESSION:
            return regression_ct(
                self.options.temperature_celsius,
                self.options.ph,
                self.options.concentration_mg_per_liter,
            )

    def calculate_log_inactivation_ratio(self, target: DisinfectionTarget):
        return self.calculate_ct() / self.required_ct(target)

    def calculate_log_inactivation(self, target: DisinfectionTarget):
        if target == DisinfectionTarget.GIARDIA:
            return 3 * self.calculate_log_inactivation_ratio(target)
        elif target == DisinfectionTarget.VIRUSES:
            return 4 * self.calculate_log_inactivation_ratio(target)

        return 1 - self.calculate_inactivation_ratio(
            concentration_mg_per_liter, target, agent
        )

    def analyze(self, target: DisinfectionTarget):
        results = {}
        results["tdt"] = self.calculate_tdt()
        results["contact_time"] = self.calculate_contact_time()
        results["required_ct"] = self.required_ct(target)
        results["calculated_ct"] = self.calculate_ct()
        results["ct_ratio"] = self.calculate_log_inactivation_ratio(target)
        results["log_inactivation"] = self.calculate_log_inactivation(target)
        return results


def NoTableEntryError(Exception):
    pass
