# EchoChamber

EchoChamber is a project that creates AI-powered Discord bots that can converse with each other and with humans in a Discord channel. These bots are built using OpenAI's GPT-3.5 model and the Discord API, and they provide engaging and interactive conversations with users.

![illustration](illustration.png)

## Table of Contents

- [EchoChamber](#echochamber)
  - [Table of Contents](#table-of-contents)
  - [1. Introduction](#1-introduction)
    - [Project Purpose](#project-purpose)
    - [Technologies Used](#technologies-used)
  - [2. Getting Started](#2-getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation \& Setup](#installation--setup)
    - [Running the AI Discord Bots](#running-the-ai-discord-bots)
  - [3. Features](#3-features)
    - [Conversations with AI Discord Bots](#conversations-with-ai-discord-bots)
    - [AI Bots Conversing with Each Other](#ai-bots-conversing-with-each-other)
      - [Personalities](#personalities)
  - [4. Customization](#4-customization)
    - [Choosing AI Personalities](#choosing-ai-personalities)
    - [Sleep Time Configuration](#sleep-time-configuration)
  - [1. Code Overview](#1-code-overview)
    - [Main Files](#main-files)
    - [Project Structure](#project-structure)

## 1. Introduction

### Project Purpose

The purpose of this project is to showcase the capabilities of AI language models in real-time conversations and provide an interactive experience for Discord users. By allowing users to interact with AI-powered bots with various personalities, the project aims to create engaging and enjoyable conversations.

### Technologies Used

- Python
- Discord API
- OpenAI gpt-3.5-turbo model

## 2. Getting Started

### Prerequisites

- Python 3.7 or later
- Discord account
- Discord Developer Portal access for creating a bot
- OpenAI API key

### Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/adamyodinsky/EchoChamber.git
```

2. Change into the project directory:

```bash
cd echochamber
```

3. Install the required dependencies using Poetry:

```bash
poetry install
```

4. Create a .env file in the project root directory, and add your Discord bot token and OpenAI API key:

```bash
DISCORD_BOT_TOKEN=your_bot_token
OPENAI_API_KEY=your_openai_api_key
```

### Running the AI Discord Bots

To run the AI Discord bot with a default personality and sleep time, use the following command:

```bash
poetry run python main.py
```

For customization, you can use the commands specified in the makefile.

## 3. Features

### Conversations with AI Discord Bots

Users can engage in conversations with the AI Discord bots. The bots are powered by OpenAI's GPT-3.5 model and provide realistic, human-like responses.

### AI Bots Conversing with Each Other

The AI bots can also converse with each other, providing an interesting and dynamic conversation experience for the users in the channel.

#### Personalities

The AI bots have different personalities that users can choose from. These personalities are defined in the personalities.py file.

## 4. Customization

### Choosing AI Personalities

To run the bot with a specific personality, use the PERSONALITY environment variable followed by the desired personality type:

```bash
PERSONALITY=interesting poetry run python main.py
```

### Sleep Time Configuration

You can configure the sleep time between messages by using the SLEEP_TIME environment variable:

```bash
SLEEP_TIME=2 poetry run python main.py
```

## 1. Code Overview

### Main Files

- main.py: Contains the main logic for the AI Discord bots.
- makefile: Provides easy-to-use commands for running the bots with different configurations.

### Project Structure

```markdown
echochamber/
├── .env
├── main.py
├── makefile
├── llm/
│   ├── __init__.py
│   ├── ...
└── personalities/
    ├── __init__.py
    ├── personalities_map.py
```
