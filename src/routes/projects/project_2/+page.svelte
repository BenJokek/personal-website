<script>
    import plane3 from "../../../lib/images/plane3.png";
    import Description from "../Description.svelte";
</script>

<Description
    title="Analysis of Airplane Crashes and Aviation Safety"
    description="This project focuses on analyzing historical data related to airplane crashes and flights to gain insights into the nature of airplane crashes and the ongoing efforts to enhance aviation safety."
    images={[plane3]}
    date="May 2023 - May 2023"
    project_link="https://github.com/BenJokek/Henry-inidividual-project-2"
    skills={["Tableau", "Python", "Matplotlib", "Seaborn"]}
>
    <p>
        This project focuses on analyzing historical data related to airplane
        crashes and flights to gain insights into the nature of airplane crashes
        and the ongoing efforts to enhance aviation safety.
    </p>
    <p>
        Two datasets were utilized: one containing records of major airplane
        accidents over the past 110 years and another containing records of
        flights over the past 50 years.
    </p>
    <h3>Data Cleaning Process:</h3>
    <ul>
        <li>
            Both datasets underwent a data cleaning process to ensure data
            clarity and consistency.
        </li>
    </ul>

    <h3>Findings:</h3>

    <ul>
        <li>
            The number of plane accidents since 1908 is approximately 5,000,
            including both military and non-military flights.
        </li>
        <li>Over 111,000 lives have been lost in these accidents.</li>
        <li>
            The year 1972 was the deadliest year for plane crashes, with 77
            crashes resulting in nearly 2,800 deaths.
        </li>
        <li>
            There was a slightly higher number of crashes during winter seasons
            and fewer crashes during early hours.
        </li>
        <li>
            The analysis of a dataset from the World Bank indicated a decreasing
            trend in crashes when considering the rise in total flights.
        </li>
        <li>
            Russian Airlines, Aeroflot, has the highest frequency of crashes
            (253) among commercial airlines.
        </li>
        <li>
            The Douglas DC-3 planes were involved in the highest number of
            crashes (330) primarily in the years following World War II. Despite
            the number of crashes, the DC-3 was considered advanced for its
            time.
        </li>
    </ul>
    <h3>Conclusions:</h3>
    <ul>
        <li>
            There has been a notable decrease in airplane crashes and fatalities
            over time, despite the increase in the number of passengers.
        </li>
        <li>
            The aviation industry has made significant progress in enhancing
            safety measures and protocols, resulting in improved safety
            standards.
        </li>
        <li>
            Ongoing efforts, such as research, technology advancements,
            training, and collaborative initiatives, are necessary to further
            enhance aviation safety.
        </li>
    </ul>
    <p>
        In summary, while air travel has become safer over time, continuous
        improvement and vigilance are vital to maintaining and further improving
        safety standards in the aviation industry.
    </p>
    <br />
    <a
        href="https://public.tableau.com/app/profile/benjamin8790/viz/Airplanecrashes_16847360071820/Story1"
        target="_blank">Tableau Dashboard</a
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
