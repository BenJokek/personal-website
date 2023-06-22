<script>
	import { dev } from "$app/environment";
	import { inject } from "@vercel/analytics";

	inject({ mode: dev ? "development" : "production" });
	
	import Header from "./Header.svelte";
	import "./styles.css";
	import bgvideo from "../lib/images/backgroundvideo.mp4";
</script>

<div class="app">
	<Header />

	<main>
		<slot />
	</main>

	<video autoplay muted loop id="myVideo">
		<source src={bgvideo} type="video/mp4" />
	</video>

	<!-- <footer>
	</footer> -->
</div>

<style>
	@import url("https://fonts.googleapis.com/css2?family=Varela+Round&display=swap");

	.app {
		min-height: 100vh;
		background: linear-gradient(
			to bottom,
			rgba(0, 0, 0, 0.65),
			rgba(0, 0, 0, 0.75)
		);
	}

	/* Style the video: 100% width and height to cover the entire window */
	#myVideo {
		position: fixed;
		right: 0;
		bottom: 0;
		min-width: 100%;
		min-height: 100%;
		z-index: -1;
	}
</style>
