<script>
    import pb from "../../store";

    let inputEmail;
    let inputPassword;

    async function handleOnSubmit() {
        try {
            const recordLogin = await pb.collection('Users').authWithPassword(inputEmail, inputPassword);
        } catch(e) {
            console.log(e);
        }
    }
</script>

<form on:submit|preventDefault={handleOnSubmit} class="m-5 p-5 rounded-lg border-2 border-gray">
    <div>
        <label>
            Email:
            <input id="email" bind:value={inputEmail} type="text" class="m-2 border-2 border-gray rounded">
        </label>
    </div>
    <div>
        <label>
            Password:
            <input id="password" bind:value={inputPassword} type="password" class="m-2 border-2 border-gray rounded">
        </label>
    </div>
    <button type="submit" class="border rounded p-2">
        Login
    </button>
</form>