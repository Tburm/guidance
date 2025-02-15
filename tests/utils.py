import guidance
import pytest

opanai_model_cache = {}

def get_openai_llm(model_name, caching=False):
    """ Get an OpenAI LLM with model reuse and smart test skipping.
    """

    # we cache the models so lots of tests using the same model don't have to
    # load it over and over again
    key = model_name+"_"+str(caching)
    if key not in opanai_model_cache:
        opanai_model_cache[key] = guidance.llms.OpenAI(model_name, caching=caching)
    llm = opanai_model_cache[key]

    if llm.token is None:
        pytest.skip("OpenAI token not found")

    return llm

transformers_model_cache = {}

def get_transformers_llm(model_name, caching=False):
    """ Get an OpenAI LLM with model reuse.
    """

    # we cache the models so lots of tests using the same model don't have to
    # load it over and over again
    key = model_name+"_"+str(caching)
    if key not in transformers_model_cache:
        transformers_model_cache[key] = guidance.llms.Transformers(model_name, caching=caching)

    return transformers_model_cache[key]

llamacpp_model_cache = {}

def get_llamacpp_llm(model_name, caching=False):
    """ Get a llama.cpp LLM with model reuse.
    """

    # we cache the models so lots of tests using the same model don't have to
    # load it over and over again
    key = model_name+"_"+str(caching)
    if key not in llamacpp_model_cache:
        settings = guidance.llms.LlamaCppSettings()
        settings.model = model_name
        llamacpp_model_cache[key] = guidance.llms.LlamaCpp(settings, caching=caching)

    return llamacpp_model_cache[key]