# hello-world--ai--2024

goals
[x] go through https://9elements.com/blog/ai-glossary/
[x] go through https://platform.openai.com/docs/introduction/key-concepts
[x] go through https://ai-guide.future.mozilla.org/
[] https://cookbook.openai.com/
[] ask DDC about his GPT
[] scene -- meetup
understand real world cases from https://huggingface.co/support
  [] fine tune
  [] optimize for low latency
  [] optimize prod env
  [] sagemaker
  [] bias
[] ChatGPT plugins https://github.com/openai/plugins-quickstart
[] go through https://app.datacamp.com/workspace/w/2da1f6ee-4d26-474f-b8f1-1ed72ed1596d/edit
[] agents?? https://www.artifact.io/iap
[] how does this work? https://github.com/ykhli/AI-tamago/blob/main/src/app/utils/interaction.ts
[] https://9elements.com/blog/using-symbolic-logic-for-mitigating-nondeterministic-behavior-and-hallucinations-of-llms/
[] distillation https://github.com/genezc/minima
[] ML system design https://www.evidentlyai.com/ml-system-design
[] tool https://erichartford.com/running-dolphin-locally-with-ollama
[] https://blog.gregbrockman.com/how-i-became-a-machine-learning-practitioner
[] https://agentydragon.com/posts/2023-01-11-how-i-got-to-openai.html
[] https://github.blog/2023-10-30-the-architecture-of-todays-llm-applications/
[] https://www.anaconda.com/definitive-guide-to-ai-platforms
[] new generated profile picture
[] https://cookbook.openai.com/



Productionization of a LLM:
[] fine tuning https://asmirnov.xyz/doppelganger https://www.sbert.net/docs/training/overview.html https://platform.openai.com/docs/guides/fine-tuning
[] RAG https://medium.com/@rushing_andrei/building-a-basic-rag-retrieval-augmented-generation-system-in-a-rails-app-247ccce5d1d2
https://modal.com/blog/embedding-wikipedia


[] Make a GPT https://openai.com/blog/introducing-gpts
[] https://openai.com/blog/introducing-the-gpt-store


```bash
source .venv/bin/activate
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip         ## pip upgrade itself
python3 -m pip install --upgrade setuptools  ## update setuptools

...

deactivate
```

```bash
## prerequisites
brew install cmake
alias nproc="sysctl -n hw.logicalcpu"
## https://pytorch.org/get-started/locally/
WHICH VERSION???
conda install pytorch torchvision -c pytorch
pip install torch -f https://download.pytorch.org/whl/torch_stable.html

## install huggingface's transformers library
## https://ai-guide.future.mozilla.org/content/choosing-ml-models/
pip install transformers sentencepiece


````

```bash

## https://huggingface.co/welcome
pip install huggingface_hub


````



```bash
virtualenv .venv

```




See also
* 2023 LLM course https://github.com/mlabonne/llm-course
* https://zapier.com/blog/best-ai-courses/
