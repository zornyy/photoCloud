<script>
    import Register from "./register.svelte";
    import Login from "./login.svelte";

    let register = false;

    function changeMode() {
        register = !register;
    }
</script>

{#if register}
    <Register/>
    <div>Already have an account ? <button on:click={changeMode}>Login</button></div>
{:else}
    <Login/>
    <div>Do not have any account ? <button on:click={changeMode}>Register</button></div>
{/if}

