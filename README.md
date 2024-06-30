# NewsletterGen Crew with GUI

Welcome to my NewsletterGen Crew project, powered by [crewAI](https://crewai.com). I designed this template to help set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. My goal is to enable agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.


## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/newsletter_gen/config/agents.yaml` to define your agents
- Modify `src/newsletter_gen/config/tasks.yaml` to define your tasks
- Modify `src/newsletter_gen/crew.py` to add your own logic, tools and specific args
- Modify `src/newsletter_gen/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
poetry run newsletter_gen
```

This command initializes the newsletter-gen Crew, assembling the agents and assigning them tasks as defined in your configuration.

![crewai-newsletter](https://github.com/EfthimiosVlahos/MultiAgent-NewsletterGen/assets/56899588/f1189f97-fee4-4b7c-888f-3cda43b865d3)


## Objective

The newsletter-gen Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.


## Conclusion

This project demonstrates my ability to leverage multi-agent AI systems using crewAI. By creating a streamlined and efficient template for newsletter generation, I have shown proficiency in setting up, customizing, and managing collaborative AI agents to perform complex tasks. The project highlights practical applications in automating content creation, improving information dissemination, and enhancing decision-making processes.

![process](https://github.com/EfthimiosVlahos/MultiAgent-NewsletterGen/assets/56899588/3ab359bf-a1c6-47b1-ba66-a0c2d5ecbbae)

