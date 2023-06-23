<script>
    import { onMount } from 'svelte';
  
    let name = '';
    let email = '';
    let subject = '';
    let message = '';
  
    async function submitForm() {
      const response = await fetch('/api/submit-form', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email, subject, message })
      });
  
      const result = await response.json();
      console.log(result);
    }
  
    onMount(() => {
      // Perform any initialization logic here
    });
  </script>
  
  <main>
    <form on:submit|preventDefault={submitForm}>
      <input type="text" bind:value={name} placeholder="Name" required />
      <input type="email" bind:value={email} placeholder="Email" required />
      <input type="text" bind:value={subject} placeholder="Subject" required />
      <textarea bind:value={message} placeholder="Message" required></textarea>
      <button type="submit">Submit</button>
    </form>
  </main>
  