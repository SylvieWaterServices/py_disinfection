"""Main module."""

from enum import Enum
import tables


class DisinfectantAgent(Enum):
    FREE_CHLORINE = 1
    CHLORINE_DIOXIDE = 2
    CHLORAMINES = 3


class DisinfectionTarget(Enum):
    VIRUSES = 1
    GIARDIA = 2


class CTReqEstimator(Enum):
    CONSERVATIVE = 1
    INTERPOLATION = 2
    REGRESSION = 3


class DisinfectionSegmentOptions:
    agent: DisinfectantAgent = DisinfectantAgent.FREE_CHLORINE
    ctreq_estimator: CTReqEstimator = CTReqEstimator.CONSERVATIVE
    volume_gallons: float
    temperature_celsius: float
    ph: float
    concentration_mg_per_liter: float
    baffling_factor: float = 0.3
    default_theoretical_detention_time_minutes: float
    peak_hourly_flow_gallons_per_minute: float


class DisinfectionSegment:
    def __init__(options: DisinfectionSegmentOptions):
        options = options

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

    def calculate_ct(self, concentration_mg_per_liter=None):
        if concentration_mg_per_liter is None:
            concentration_mg_per_liter = self.options.default_concentration_mg_per_liter
        return self.calculate_contact_time() * concentration_mg_per_liter

    def required_ct(
        self,
        target: DisinfectionTarget = "GIARDIA",
        agent: DisinfectantAgent = "FREE_CHLORINE",
    ):
        if target == DisinfectionTarget.GIARDIA:
            return self._required_ct_giardia(agent)
        elif target == DisinfectionTarget.VIRUSES:
            return self._required_ct_viruses(agent)

    def _required_ct_giardia(self, agent: DisinfectantAgent = "FREE_CHLORINE"):
        if agent == DisinfectantAgent.FREE_CHLORINE:
            return self._required_ct_giardia_free_chlorine()
        elif agent == DisinfectantAgent.CHLORINE_DIOXIDE:
            return self._required_ct_giardia_chlorine_dioxide()
        elif agent == DisinfectantAgent.CHLORAMINES:
            return self._required_ct_giardia_chloramines()
        return None

    def _required_ct_viruses(self, agent: DisinfectantAgent = "FREE_CHLORINE"):
        if agent == DisinfectantAgent.FREE_CHLORINE:
            return self._required_ct_viruses_free_chlorine()
        elif agent == DisinfectantAgent.CHLORINE_DIOXIDE:
            return self._required_ct_viruses_chlorine_dioxide()
        elif agent == DisinfectantAgent.CHLORAMINES:
            return self._required_ct_viruses_chloramines()
        return None

    def _roundDownToNearest(self, x, base=5):
        return base * math.floor(x / base)

    def _roundUpToNearest(self, x, base=5):
        return base * math.ceil(x / base)

    def _required_ct_giardia_free_chlorine(self):
        # table is [maxC][concentration][maxpH]
        table = tables.giardia_3log_ct_values_free_chlorine
        if self.ctreq_estimator == CTReqEstimator.CONSERVATIVE:
            # Round to nearest multiple of 5 degrees
            estimated_temperature = self._roundDownToNearest(
                self.options.temperature_celsius, 5
            )
            if estimated_temperature > 25:
                estimated_temperature = 25
            if estimated_temperature < 5:
                estimated_temperature = 0.5

            estimated_ph = self._roundUpToNearest(self.options.ph, 0.5)
            estimated_concentration = self._roundUpToNearest(
                self.options.concentration_mg_per_liter, 0.2
            )
        # elif self.ctreq_estimator == CTReqEstimator.INTERPOLATION:
        #     high_temperature = self._roundUpToNearest(self.options.temperature_celsius, 5)
        #     low_temperature = self._roundDownToNearest(self.options.temperature_celsius, 5)
        #     if high_temperature > 25:
        #         high_temperature = 25
        #     if low_temperature < 5:
        #         low_temperature = 0.5
        #     high_ph = self._roundUpToNearest(self.options.ph, 0.5)
        #     low_ph = self._roundDownToNearest(self.options.ph, 0.5)
        #     high_concentration = self._roundUpToNearest(
        #         self.options.concentration_mg_per_liter, 0.2
        #     )
        #     low_concentration = self._roundDownToNearest(
        #         self.options.concentration_mg_per_liter, 0.2
        #     )
        #     estimated_temperature =

        try:
            ct_req = table[estimated_temperature][estimated_concentration][estimated_ph]
        except IndexError:
            raise NoTableEntryError(
                f"No table entry for temperature {estimated_temperature}, concentration {estimated_concentration}, and pH {estimated_ph}"
            )
        return ct_req

    def calculate_log_inactivation_ratio(
        self,
        concentration_mg_per_liter=None,
        target: DisinfectionTarget = "GIARDIA",
        agent: DisinfectantAgent = "FREE_CHLORINE",
    ):
        return self.calculate_ct(concentration_mg_per_liter) / self.required_ct(
            target, agent
        )

    def calculate_log_inactivation(
        self,
        concentration_mg_per_liter=None,
        target: DisinfectionTarget = "GIARDIA",
        agent: DisinfectantAgent = "FREE_CHLORINE",
    ):
        if target == DisinfectionTarget.GIARDIA:
            return 3 * self.calculate_log_inactivation_ratio(
                concentration_mg_per_liter, target, agent
            )
        elif target == DisinfectionTarget.VIRUSES:
            return 4 * self.calculate_log_inactivation_ratio(
                concentration_mg_per_liter, target, agent
            )

        return 1 - self.calculate_inactivation_ratio(
            concentration_mg_per_liter, target, agent
        )


def NoTableEntryError(Exception):
    pass
