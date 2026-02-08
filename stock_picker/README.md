# StockPicker Crew

Welcome to the Stock Picker Crew project, powered by [crewAI](https://crewai.com).

Multi-Agent System with Parallel workflow
Manager Agent coordinates work through 3 specialized agents
    * trending_company_finder
    * financial_researcher
    * stock_picker
and tasks
    * find_trending_companies
    * research_trending_companies
    * pick_best_company

Custom Tool
    * PushNotificationTool - send push through PushOver
    * send to agent constructor

Define Structured Outputs for task results
    * TrendingCompanyResearch(BaseModel)
    * send to task constructor

Create crew
    * define manager Agent
    * set process to hierarchical through crew constructor
    * set manager_agent through crew constructor

Update main
    * clear template
    * set input variable for kickoff

## Installation

## Running the Project
