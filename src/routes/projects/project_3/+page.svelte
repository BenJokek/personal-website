<script>
    import movies from "../../../lib/images/movies.jpg";
    import Description from "../Description.svelte";
</script>

<Description
    title="Movie Recommendation System"
    description="Overall, this project involved data engineering, API development using FastAPI, content-based recommendation model implementation, and a Streamlit app for user interaction."
    images={[movies]}
    date="May 2023 - May 2023"
    project_link="https://github.com/BenJokek/Henry-individual-project-1"
    skills={["Machine Learning", "FastAPI", "SQL", "Python", "Streamlit"]}
>
    <p>
        Overall, this project involved data engineering, API development using
        FastAPI, content-based recommendation model implementation, and a
        Streamlit app for user interaction.
    </p>
    <p>
        In this project, as a MLOps Engineer working at a streaming platform
        aggregation service startup, I was tasked with creating a recommendation
        system from scratch. The existing data had low maturity, with nesting
        and lack of transformation.
    </p>
    <p>
        To address these issues and develop a Minimum Viable Product (MVP)
        within a week, I followed the following steps:
    </p>
    <h3>ETL (Extract, Transform, Load):</h3>
    <ul>
        <li>Imported the dirty data from the datasets directory.</li>
        <li>
            Exported the cleaned data as a ".csv" file for later use in the
            recommendation system.
        </li>
        <li>Performed data cleaning and transformation.</li>
        <li>
            Uploaded the cleaned data to a PostgreSQL database hosted on Render.
        </li>
    </ul>
    <h3>FastAPI:</h3>
    <ul>
        <li>
            Created a web application using the FastAPI framework, which served
            as the backend for the recommendation system.
        </li>
        <li>
            Implemented several endpoints that interacted with the PostgreSQL
            database using SQLAlchemy to perform operations on movie data.
        </li>
        <li>
            Hosted the API on Render, configuring environment variables with the
            database credentials.
        </li>
    </ul>
    <h3>API Goals:</h3>
    <ul>
        <li>
            Developed several API endpoints to achieve specific goals, such as
            retrieving the number of movies released in a given month or on a
            specific day of the week historically, obtaining movie statistics by
            franchise, country, producer, or individual movie, and generating a
            recommended list of similar movies based on a given movie name.
        </li>
    </ul>
    <h3>Movie Description-Based Recommender Model:</h3>
    <ul>
        <li>
            Implemented a content-based filtering/recommender system based on
            movie metadata, specifically using movie "Overviews" and "Taglines."
        </li>
        <li>
            Retrieved all movies from the PostgreSQL database using the FastAPI
            app.
        </li>
        <li>
            Preprocessed the movie data and computed cosine similarity between
            their descriptions to generate a list of recommended movies for a
            given title.
        </li>
    </ul>

    <br />
    <a href="https://www.youtube.com/watch?v=jDqP0YQ24PM" target="_blank"
        >Video</a
    ><br />
    <a
        href="https://benjokek-henry-individual-project-1-streamlit-qc9jn6.streamlit.app/"
        target="_blank">Streamlit</a
    ><br />
</Description>

<style>
    p {
        color: #cfcdcd;
        font-size: 16px;
        margin-bottom: 15px;
        line-height: 1.5;
    }
    a {
        color: #0088cc;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    ul {
        color: #cfcdcd;
    }
    li {
        margin: 10px;
    }
    h3 {
        color: aliceblue;
        font-size: 1.5rem;
        margin: 12px;
    }
</style>
