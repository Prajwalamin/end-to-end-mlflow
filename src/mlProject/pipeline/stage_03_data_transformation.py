from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_transformation import DataTransformation
from pathlib import Path
from src.mlProject import logger


STAGE_NAME = "Data Transformation stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitter()

            else:
                raise Exception("Your data schema is not valid. Please validate your data first.")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")
        pipeline = DataTransformationTrainingPipeline()
        pipeline.main()
        logger.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logger.exception(e)
        raise e
