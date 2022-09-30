from fhirclient.models import (
    explanationofbenefit, fhirreference, money
)


class ExplanationOfBenefit(explanationofbenefit.ExplanationOfBenefit):
    def __init__(self, jsondict=None, strict=True):
        super().__init__(jsondict, strict)
        self.hospitalization = None
        self.organization = None
        self.information = None
        self.totalCost = None

    def elementProperties(self):
        js = super(ExplanationOfBenefit, self).elementProperties()
        js.extend([
            ("hospitalization", "hospitalization", dict, False, None, False),
            ("organization", "organization", dict, False, None, False),
            ("information", "information", dict, True, None, False),
            ("totalCost", "totalCost", dict, False, None, False),
        ])
        js = list(filter(lambda x: x[0] not in [
                  'insurer', 'insurance', 'outcome', 'use', 'item'], js))

        js.extend([
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("item", "item", ExplanationOfBenefitItem, True, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("use", "use", str, False, None, False),
            ("item", "item", ExplanationOfBenefitItem, True, None, False),
            ("insurance", "insurance", ExplanationOfBenefitInsurance, True, None, False)
        ])

        # name, jsname, typ, is_list, of_many, not_optional
        return js


class Money(money.Money):
    def elementProperties(self):
        js = super(Money, self).elementProperties()
        return js


class ExplanationOfBenefitItem(explanationofbenefit.ExplanationOfBenefitItem):
    def elementProperties(self):
        js = super(ExplanationOfBenefitItem, self).elementProperties()

        return js


class ExplanationOfBenefitInsurance(explanationofbenefit.ExplanationOfBenefitInsurance):
    def elementProperties(self):
        js = super(ExplanationOfBenefitInsurance, self).elementProperties()
        js.remove(("focal", "focal", bool, False, None, True))
        js.extend([("focal", "focal", bool, False, None, False)])
        return js

class ExplanationOfBenefitAddItem(explanationofbenefit.ExplanationOfBenefitAddItem):
    def elementProperties(self):
        js = super(ExplanationOfBenefitItem, self).elementProperties()
        js.extend([])
        return js