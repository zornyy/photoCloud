<script>
    import {pb} from "../../store";


    let inputName;
    let inputUsername;
    let inputEmail;
    let inputPassword;
    let inputPasswordConfirm

    async function handleOnSubmit() {
        console.log("Registering");
        const data = {
            name : inputName,
            username : inputUsername,
            password : inputPassword,
            passwordConfirm : inputPasswordConfirm,
            email : inputEmail,
        };

        try {
            const record = await pb.collection('Users').create(data);
            const recordLogin = await pb.collection('Users').authWithPassword(inputEmail, inputPassword);
        } catch(e) {
            console.log(e);
        }
    }
</script>


<form on:submit|preventDefault={handleOnSubmit} class="m-5 p-5 rounded-lg border-2 border-gray">
    <div>
        <label class="flex flex-column items-center">
            <div>Full name:</div>
            <input id="name" bind:value={inputName} type="text" class="m-2 border-2 border-gray rounded">
        </label>
    </div>
    <div>
        <label>
            Username:
            <input id="username" bind:value={inputUsername} type="text" class="m-2 border-2 border-gray rounded">
        </label>
    </div>
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
    <div>
        <label>
            Confirm password:
            <input id="confirm_password" bind:value={inputPasswordConfirm} type="password" class="m-2 border-2 border-gray rounded">
        </label>
    </div>
    <button type="submit" class="border rounded p-2">
        Register
    </button>
</form>