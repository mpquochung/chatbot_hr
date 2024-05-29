


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="image/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">CV finder</h3>

  <p align="center">
    This project is aim to search for suitable applicant base on request of HR base on a LLM system. The user (HR) can chat with the app interface.
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#architecture">Architecture</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

"HR Chatbot" is a cutting-edge application that revolutionizes the recruitment process. It leverages Langchain and AWS services to create a chatbot that interacts with HR professionals. The chatbot uses a Language Model (LLM) to understand HR requests and search for suitable job applicants. Users can chat with the application, inputting their specific requirements, and the chatbot will provide the most relevant candidate profiles. This application simplifies the recruitment process, making it more efficient and user-friendly.


### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Str][Streamlit]][Streamlit-url]
* ![bucket][S3]
* ![db][RDS]
* ![instace][EC2]
* ![embedding][OPENAI]
* ![llm][claude]
* ![dbms][pg]

<!-- Architecture -->
## Architecture
See the architecture of the chat backend as follow for easy visualization.
![backend-architecture][architecture]


1. **Decider** (Claude3 Haiku): Determines whether to initiate a normal conversation or start the process to search for suitable CVs.
2. **Normal Chat** (Claude3 Haiku): Initiates a conversation with LLM when a normal chat is invoked by the Decider.
3. **Retransforming Queries** (Claude3 Sonnet): Transforms user prompts into more accurate queries for finding suitable applicants by generating different variations. This helps improve search accuracy. For example, a complex query like “I want to find a Backend developer with over 5 years of experience and expertise in Java Springboot and Node.js” is broken down into simpler queries.
4. **Semantic Search** (pgvector): Uses the transformed queries to perform a semantic search for CVs that match the HR requirements.
5. **Top k CVs**: Identifies the top k most suitable CVs based on a predefined threshold or relevance score. These initial results may require further refinement.
6. **Reranking** (Cohere rerank3 on Sagemaker): Uses a reranking model to evaluate and refine the top k CVs to identify the top 5 best candidates using the Cohere Command model hosted on AWS SageMaker.
7. **Reasoning** (Claude3 Sonnet): The final stage involves providing a summary and analysis of the top-ranked CVs, highlighting key skills, experiences, past projects, achievements, and educational background. The LLM offers a recommendation on whether to shortlist or reject each candidate, with justifications to support informed decision-making.
<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

The configuration is complicated to implement since everything is on the Cloud! Here are prerequisites of the app:
* OPENAI API
* AWS Bedrock Foundation Models Access (Claude-3-haiku, Claude-3-Sonnet)
* AWS S3
* AWS RDS: PostgresSQL database & pgvector
* AWS Sagemaker: Cohere-rerank-multilingual-3 endpoint
* AWS EC2 instance

### Installation

_Below are steps how you can install the app. Assuming that you have all access to the prerequisites._

1. Clone the repo
   ```sh
   git clone https://github.com/mpquochung/chatbot_hr.git
   ```
2. Change directory into the root folder
   ```sh
   cd chatbot_hr
   ```
3. Install all required library
   ```py
   !pip install requirements.txt
   ```
4. Create ".env" file and config your ".env" up to the example in ".env.example"
   ```py
   OPENAI_API_KEY= 'Enter your API key'
   PGVECTOR_WRITER_HOST = 'Enter pgvector endpoint'
   ...
   ```

<!-- USAGE EXAMPLES -->
## Usage
### Start app
To start with, first you must execute the streamlit function to start the app.
   ```sh
   streamlit run Home.py --server.port 8080 
   ```
### How to use
1. Go to the 'Upload CV' page.
2. Upload CV files in one of the following formats: docx, doc, pdf, xlsx.
3. Go to "CV management" page to verify if the CV is well handled. 
4. Enter the chatbot and feel free to try it out. You can ask anything about the CV.


<!-- ROADMAP -->
## Roadmap

- [x] Build chat-backend
- [x] Build chat user interface
- [x] Deploy
- [ ] Prompt engineering
- [ ] Graph-base query


See the [open issues](https://github.com/mpquochung/chatbot_hr/issues) for a full list of proposed features (and known issues).




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.



<!-- CONTACT -->
## Contact

Mai Phan Quốc Hưng - [@linkedin](https://www.linkedin.com/in/qhungmp/) - maphquochung@gmail.com

Project Link: [github](https://github.com/mpquochung/chatbot_hr.git) 



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This project is inherrited from many source. Here are some soure to reference:

* [Agent](https://github.com/aws-samples/aws-agentic-document-assistant)
* [pgvector](https://aws.amazon.com/vi/blogs/database/leverage-pgvector-and-amazon-aurora-postgresql-for-natural-language-processing-chatbots-and-sentiment-analysis/)
* [workshop](https://github.com/aws-samples/amazon-bedrock-workshop)

Finally, I want to express my appreciation to those who support me in this project. Without their discussions about the product and support in configuring AWS services and the database, I could not have completed this project successfully.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/mpquochung/chatbot_hr/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/qhungmp/
[product-screenshot]: image/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[Streamlit]: https://img.shields.io/badge/Streamlit-%23FF4B4B?logo=streamlit&color=white
[Streamlit-url]: https://streamlit.io
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[S3]: https://img.shields.io/badge/AWS%20S3-%23569A31?logo=amazons3&color=white
[RDS]: https://img.shields.io/badge/AWS%20RDS-%23569A31?logo=amazonrds&color=white
[EC2]: https://img.shields.io/badge/AWS%20EC2-%23569A31?logo=amazonec2&color=white
[OPENAI]: https://img.shields.io/badge/OPENAI%20API-%23412991?logo=openai&logoColor=%23412991&color=white
[Claude]: https://img.shields.io/badge/AWS%20Bedrock%20Claude3-%23191919?logo=anthropic&logoColor=%23191919&color=white
[pg]: https://img.shields.io/badge/Postgres%20SQL-%234169E1?logo=postgresql&logoColor=%234169E1&color=white
[architecture]: image/architecture.png
