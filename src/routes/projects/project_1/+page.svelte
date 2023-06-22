<script>
    import stack from "../../../lib/images/stack.png";
    import Description from "../Description.svelte";
</script>

<Description
    title="Data-Driven Analysis of User Opinion for Investment Opportunities in the
US Personal Care and Aesthetics Industry"
    description="Data-Driven Analysis of User Opinion for Investment
    Opportunities in the US Personal Care and Aesthetics
    Industry"
    images={[stack]}
    date="Jun 2023 - Jun 2023"
    project_link="https://github.com/BenJokek/Final-Project-Data-Science"
    skills={[
        "Google Cloud Platform (GCP)",
        "PySpark",
        "Agile Methodologies",
        "Git",
        "Python",
    ]}
>
    <p>
        As a Data Engineer, my main role involved setting up and managing the
        ETL process for the project. I activated the Drive API and created
        credentials to access data from Google Drive. I transferred data from
        Google Drive to Google Cloud Storage (GCS) and performed data
        transformation using the Dataflow Workbench. I stored the transformed
        data in GCS and loaded it into BigQuery. Documentation of code and steps
        was important throughout the process. My role was essential in ensuring
        smooth data flow, transformation, and availability for analysis.
    </p>
    <p>
        Using sentiment analysis techniques and machine learning, we collected
        and analyzed data to determine the most suitable locations for
        establishing new business premises and uncover investment opportunities.
        By considering factors like market growth, demand for beauty services,
        competition, and emerging trends, we provided clear and well-founded
        recommendations for investors in the Latin American aesthetic industry.
    </p>
    <p>
        Through sentiment analysis, we classified reviews as positive, negative,
        or neutral, enabling us to identify states with the happiest customers.
        Additionally, we employed clustering techniques based on geographic
        locations and average ratings to understand the competition landscape in
        each area. By analyzing state, county, average scores, and competition
        percentages, we presented insights to make informed investment
        decisions.
    </p>
</Description>

<style>
    p {
        color: #cfcdcd;
        font-size: 16px;
        margin-bottom: 15px;
        line-height: 1.5;
    }
</style>
