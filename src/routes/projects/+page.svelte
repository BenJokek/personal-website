<script>
	import project_1 from "../../lib/images/Investment_Opportunities.jpg";
	import plane1 from "../../lib/images/plane2.png";
	import api from "../../lib/images/api.png";

	import Card from "./Card.svelte";
</script>

<svelte:head>
	<title>Projects</title>
	<meta name="description" content="About this app" />
</svelte:head>

<div class="container">
	<Card
		title="Data-Driven Analysis of User Opinion for Investment Opportunities in the US Personal Care and Aesthetics Industry"
		image={project_1}
		project="project_1"
	/>

	<Card
		title="Analysis of Airplane Crashes and Aviation Safety"
		image={plane1}
		project="project_2"
	/>

	<Card title="Movie Recommendation System" image={api} project="project_3"/>
</div>

<style>
	.container {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
		align-items: center;
	}

</style>
