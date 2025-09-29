# Final Project

Your goal is to create an AI agent that can understand a user's question, use a set of tools to work with a database, and produce a smart answer.
The project is all about making an AI that can interact with data in a useful way. You get to pick any database you're interested in, on any subject you like!

## Project Details

**Teams**: You'll work in groups of 3.

**By November 10th, one person from your group needs to email Kevin and me, listing all the members of your team and a brief outline of your project's pipeline.**

**Oral Presentation**: The presentation will be on **January 12th**, starting at **9:00 AM**.


# What You'll Build

You're going to set up an AI agent that connects a Large Language Model with a custom set of tools you code yourself. The agent's job is to take a simple question in plain text, figure out which tools to use, interact with a database, process the information, and give back a complete answer. Your job is mainly to create the different tools available for the agent.

## What Your Agent Should Be Able to Do

Your agent should be able to handle complex questions that require multiple steps. Here are some examples to give you an idea of the kinds of questions you could aim for:

    "Can you produce a plot with the last month's sales, broken down by day?"

    "What is the win ratio for a chess player who starts with the d4 pawn opening?"

    "Can you benchmark different algorithms for predicting Y using X variables?"

    "Can you produce a report containing the following sections: - ... ?"

    "What movies can we see in Strasbourg right now, and can you give me a summary of previous movies made by each director?"

## Building Your Agent's Toolbox 

The core of your project will be coding a set of functions in Python that the LLM can use as its tools. You are highly encouraged to use the frameworks we've covered. Your toolbox should include functions for things like:

    Querying your database (using Polars or SQL).

    Making requests to external APIs (e.g., to get movie data).

    Processing data and running calculations (Parallel or GPU programming to speed up heavy computations).

    Structure your code cleanly using Python classes.

    A cool side tool: A function that allows the LLM to commit, pull, or push code using git.

