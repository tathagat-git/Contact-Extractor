async function uploadFile() {
    const fileInput = document.getElementById("fileInput");
    const resultDiv = document.getElementById("result");

    if (!fileInput.files.length) {
        alert("Please select a file first!");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    resultDiv.innerHTML = "<p class='text-yellow-400'>Processing...</p>";

    const res = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    resultDiv.innerHTML = `
        <div class="bg-gray-800 p-4 rounded-lg">
            <h2 class="text-lg font-bold mb-2">Extracted Contacts:</h2>
            <pre class="bg-black p-3 rounded">${JSON.stringify(data, null, 2)}</pre>
        </div>
    `;
}
