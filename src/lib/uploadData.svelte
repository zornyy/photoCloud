<script>
    import pb from "../store";

    let imageToUpload;

    async function handleOnSubmit() {
        const formData = new FormData();

        const fileInput = document.getElementById('pictureInput');

        // @ts-ignore
        for (let file of fileInput.files) {
            formData.append('file', file);
        }   

        formData.append("owner", pb.authStore.model.id);
        
        try {
            const createdRecord = await pb.collection('pictures').create(formData);
            console.log("Record created");
        } catch(e) {
            console.log(e);
        }
    }
</script>

<form on:submit|preventDefault={handleOnSubmit}>
    <label>
        Picture:
        <input type="file" accept="image/*" id="pictureInput" bind:files={imageToUpload} />
    </label>
    
    <button type="submit" class="border rounded p-2">
        Upload image
    </button>
</form>