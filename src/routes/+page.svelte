<script>
	import pic from "../lib/images/my_pic.png";
	import Socials from "./Socials.svelte";
	import Button from "./Button.svelte";
	import Spinner from "./Spinner.svelte";
</script>

<svelte:head>
	<title>Benjamín Zambelli</title>
	<meta name="description" content="Ben personal website" />
</svelte:head>

<section>
	<div class="card">
		<img src={pic} alt="me" />
		<div class="info">
			<h2>Data Engineer</h2>
			<h1>Benjamín Zambelli</h1>
			<h3>Based in San Luis, Argentina</h3>
			<Socials />
			<Button />
		</div>
		<Spinner />
	</div>
</section>

<style>
	section {
		width: 100%;
		display: flex;
		justify-content: center;
	}

	.card {
		width: 90%;
		max-width: 800px;
		border-radius: 30px;
		border: 1px solid #ffffff;
		min-height: 500px;
		margin: 20px;
		box-sizing: border-box;
		color: white;
	}

	img {
		width: 200px;
		border-radius: 10%;
		display: block;
		margin: 0 auto;
	}

	.info {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		text-align: center;
	}

	h2 {
		margin-top: 10px;
		font-size: 1rem;
		margin-left: 10px;
		color: gray;
	}

	h1 {
		font-size: 2rem;
		margin-left: 10px;
	}

	h3 {
		font-size: 1rem;
		margin-left: 10px;
		color: gray;
	}

	@media (min-width: 800px) {
		.card {
			width: 50%;
		}

		section {
			width: 100%;
		}
		h2 {
			margin-top: 10px;
			font-size: 1.5rem;
			margin-left: 10px;
			color: gray;
		}

		h1 {
			font-size: 2.5rem;
			margin-left: 10px;
		}

		h3 {
			font-size: 1.5rem;
			margin-left: 10px;
			color: gray;
		}
	}
</style>
