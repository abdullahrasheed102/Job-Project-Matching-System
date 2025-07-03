from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os


load_dotenv()
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

SERPER_API_KEY=os.environ["SERPER_API_KEY"]
search_tool = SerperDevTool()




@CrewBase
class LeadGeneration():
    """LeadGeneration crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools


    @agent
    def Description_Classifier(self) -> Agent:
        return Agent(
            config=self.agents_config['Description_Classifier'], # type: ignore[index]
            verbose=True
        )

    @agent
    def PD_Analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['PD_Analyzer'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def Skill_Extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['Skill_Extractor'], # type: ignore[index]
            tools=[search_tool],
            verbose=True
        )

    @agent
    def Time_Estimator(self) -> Agent:
        return Agent(
            config=self.agents_config['Time_Estimator'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def Project_Timeline_Planner(self) -> Agent:
        return Agent(
            config=self.agents_config['Project_Timeline_Planner'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def JD_Check_point(self) -> Agent:
        return Agent(
            config=self.agents_config['JD_Check_point'], # type: ignore[index]
            verbose=True
        )

    @agent
    def JD_Analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['JD_Analyzer'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def CapabilityEvaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['CapabilityEvaluator'], # type: ignore[index]
            verbose=True
        )

    

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    

    @task
    def Description_Classifier_task(self) -> Task:
        return Task(
            config=self.tasks_config['Description_Classifier_task'], # type: ignore[index]
        )

    @task
    def PD_Analyzer_task(self) -> Task:
        return Task(
            config=self.tasks_config['PD_Analyzer_task'], # type: ignore[index]
            output_file='report.md',
            append_output=False
        )
    
    @task
    def Extract_Required_Skills(self) -> Task:
        return Task(
            config=self.tasks_config['Extract_Required_Skills'], # type: ignore[index]
            output_file='report.md',
            append_output=True
        )
    
    @task
    def Estimate_time_task(self) -> Task:
        return Task(
            config=self.tasks_config['Estimate_time_task'], # type: ignore[index]
            output_file='report.md',
            append_output=True
        )
    
    @task
    def Project_Timeline_Planner_task(self) -> Task:
        return Task(
            config=self.tasks_config['Project_Timeline_Planner_task'], # type: ignore[index]
            output_file='report.md',
            append_output=True,
        )
    
    @task
    def JD_Check_point_task(self) -> Task:
        return Task(
            config=self.tasks_config['JD_Check_point_task'], # type: ignore[index]
        )
    
    @task
    def JD_Analyzer_task(self) -> Task:
        return Task(
            config=self.tasks_config['JD_Analyzer_task'], # type: ignore[index]
        )
    
    @task
    def EvaluateDeveloperCapabilityTask(self) -> Task:
        return Task(
            config=self.tasks_config['EvaluateDeveloperCapabilityTask'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def classifier_crew(self) -> Crew:
        """Creates the Classifier crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=[
                self.Description_Classifier(),
                
            ],
            tasks=[
                self.Description_Classifier_task(),
                
            ],
            process=Process.sequential,
            verbose=True,
        )
    

    @crew
    def project_crew(self) -> Crew:
        """Creates the Project crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=[
                self.PD_Analyzer(),
                #self.Skill_Extractor(),
                #self.Time_Estimator(),
                #self.Project_Timeline_Planner(),

            ],
            tasks=[
                self.PD_Analyzer_task(),
                #self.Extract_Required_Skills(),
                #self.Estimate_time_task(),
                #self.Project_Timeline_Planner_task()
                
            ],
            process=Process.sequential,
            verbose=True,
        )
    
    @crew
    def job_crew(self) -> Crew:
        """Creates the Job crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=[
                self.JD_Analyzer(),
                self.JD_Check_point(),
                self.CapabilityEvaluator()
                
            ],
            tasks=[
                self.JD_Analyzer_task(),
                self.JD_Check_point_task(),
                self.EvaluateDeveloperCapabilityTask()
                
            ],
            process=Process.sequential,
            verbose=True,
        )






