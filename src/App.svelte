<script>
  import { pb, user } from './store';
  import { onMount } from 'svelte';
  import Auth from './lib/auth/auth.svelte';
  import UploadData from './lib/uploadData.svelte';

  let model;

  user.subscribe(value => {
    model = value;
  });

  onMount(() => {
    pb.authStore.onChange(() => {
      user.set(pb.authStore.model);
    })
  })

  async function handleOnLogout() {
    pb.authStore.clear();
    user.set(null)
  }
</script>

{#if model == null}
  <Auth/>
{:else}
  <div>
    <UploadData/>
    <button on:click={handleOnLogout} class="rounded p-2">Logout</button>
  </div>
  
{/if}

