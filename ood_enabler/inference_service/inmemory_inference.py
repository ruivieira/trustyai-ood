from ood_enabler.inference_service.inference_service import InferenceService


class InMemoryInference(InferenceService):
    def __init__(self, **kwargs):
        pass

    def infer(self, model, data_handler):
        """
        Performs inference on provided model with dataset

        :param model: model wrapper to use for inference
        :type model: `model.ModelWrapper`
        :param data_handler: data to be inferred
        :type data_handler: `data.Datahandler`
        :return: stats for normalizing data
        """
        return model.infer(data_handler)
