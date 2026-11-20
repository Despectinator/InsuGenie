from dataclasses import dataclass


@dataclass
class Patient:
    """
    Stores patient demographic and medical information.
    """

    patient_id: int

    name: str

    age: int

    gender: str

    height_cm: float

    weight_kg: float

    diabetes_type: str

    smoker: bool = False

    hypertension: bool = False