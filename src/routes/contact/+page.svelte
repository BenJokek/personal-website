<script>
	import { onMount } from "svelte";
	import * as yup from "yup";
	import Socials from "../Socials.svelte";

	const validationSchema = yup.object().shape({
		name: yup.string().required("Name is required"),
		email: yup
			.string()
			.email("Invalid email address")
			.required("Email is required"),
		subject: yup.string().required("Subject is required"),
		message: yup.string().required("Message is required"),
	});

	let name = "";
	let email = "";
	let subject = "";
	let message = "";

	let isSubmitting = false;
	let successMessage = "";

	async function handleSubmit(event) {
		event.preventDefault();

		const formData = {
			name,
			email,
			subject,
			message,
		};

		try {
			await validationSchema.validate(formData);

			isSubmitting = true;

			const response = await fetch(
				"https://contact-form-backend-2.onrender.com/submit-form",
				{
					method: "POST",
					headers: {
						"Content-Type": "application/json",
					},
					body: JSON.stringify(formData),
				}
			);

			const data = await response.json();

			name = "";
			email = "";
			subject = "";
			message = "";
			successMessage = "Form submitted successfully!";
		} catch (error) {
			console.error(error);
		} finally {
			isSubmitting = false;
		}
	}

	onMount(() => {
		console.log("Contact form mounted");
	});
</script>

<svelte:head>
	<title>Contact</title>
	<meta name="description" content="Contact Ben" />
</svelte:head>

<div class="contact">
	<Socials /><br />
	<div class="container">
		<form on:submit={handleSubmit}>
			<label for="name">Name*</label>
			<input
				type="text"
				id="name"
				bind:value={name}
				required
				placeholder="Your name (required)"
			/>

			<label for="email">Email*</label>
			<input
				type="email"
				id="email"
				bind:value={email}
				required
				placeholder="Your email (required)"
			/>

			<label for="subject">Subject*</label>
			<input
				type="text"
				id="subject"
				bind:value={subject}
				required
				placeholder="Your subject (required)"
			/>

			<label for="message">Message*</label>
			<textarea
				id="message"
				bind:value={message}
				placeholder="Your message (required)"
				required
				style="height:100px"
			/>
			<input type="submit" class="submit-button" />

			{#if isSubmitting}
				<p>Submitting...</p>
			{/if}
			{#if successMessage}
				<p>{successMessage}</p>
			{/if}
		</form>
	</div>
</div>

<style>
	.contact {
		color: white;
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.container {
		padding: 20px;
		max-width: 600px;
		margin: 0 auto;
	}

	input,
	textarea {
		width: 100%;
		padding: 12px;
		border: 3px solid #7f8683;
		border-radius: 10px;
		box-sizing: border-box;
		margin-top: 6px;
		margin-bottom: 16px;
		resize: vertical;
	}

	@media (min-width: 800px) {
		.container {
			max-width: 800px;
		}
	}

	.submit-button {
		background-color: #4caf50;
		color: white;
		padding: 10px 20px;
		border: none;
		border-radius: 4px;
		cursor: pointer;
		transition: background-color 0.3s ease;
	}

	.submit-button:hover {
		background-color: #45a049;
	}
</style>
