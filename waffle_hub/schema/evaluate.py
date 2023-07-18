from dataclasses import dataclass

from waffle_hub.schema.base_schema import BaseSchema


@dataclass
class ObjectDetectionMetric(BaseSchema):
    mAP50_95: float
    mAP50: float


@dataclass
class ClassificationMetric(BaseSchema):
    accuracy: float


@dataclass
class InstanceSegmentationMetric(BaseSchema):
    mAP50_95: float
    mAP50: float


@dataclass
class TextRecognitionMetric(BaseSchema):
    accuracy: float
