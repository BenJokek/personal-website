<script>
	import { page } from "$app/stores";

	export let title;
	export let image;
	export let project;
</script>

<a href="/projects/{project}" class:selected={$page.url.pathname === "/projects/{project}"}>
	<div class="card" style="background-image: url({image});">
		<div class="overlay">
			<h2>{title}</h2>
		</div>
	</div>
</a>

<style>
	.card {
		position: relative;
		overflow: hidden;
		min-width:300px;
		min-height: 300px;
		background-size: cover;
		background-position: center;
		margin: 30px;
	}

	.overlay {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0.6); /* Adjust the opacity as needed */
		display: flex;
		justify-content: center;
		align-items: center;
	}

	h2 {
		color: white;
		text-align: center;
		padding: 10px;
	}

	/* Media queries for responsive styles */
	@media (max-width: 768px) {
		.card {
			width: 100%;
			min-height: 200px;
			margin: 7px;
		}

		h2 {
			font-size: 1.5rem;
			padding: 5px;
		}

		a {
			width: 100%;
		}
	}
</style>
