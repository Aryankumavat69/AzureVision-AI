const fileInput = document.getElementById("fileInput");

const chooseButton =
    document.getElementById("chooseButton");

const dropArea =
    document.getElementById("dropArea");

const previewContainer =
    document.getElementById("previewContainer");

const imagePreview =
    document.getElementById("imagePreview");

const fileName =
    document.getElementById("fileName");

const removeButton =
    document.getElementById("removeButton");

const analyzeButton =
    document.getElementById("analyzeButton");

const loading =
    document.getElementById("loading");

const results =
    document.getElementById("results");

const predictionList =
    document.getElementById("predictionList");


let selectedFile = null;


/* =========================
   CHOOSE IMAGE
========================= */

chooseButton.addEventListener("click", () => {

    fileInput.click();

});


fileInput.addEventListener("change", (event) => {

    const file = event.target.files[0];

    if (file) {

        handleFile(file);

    }

});


/* =========================
   DRAG & DROP
========================= */

dropArea.addEventListener("dragover", (event) => {

    event.preventDefault();

    dropArea.style.borderColor = "#4da6ff";

});


dropArea.addEventListener("dragleave", () => {

    dropArea.style.borderColor = "#29415e";

});


dropArea.addEventListener("drop", (event) => {

    event.preventDefault();

    dropArea.style.borderColor = "#29415e";

    const file = event.dataTransfer.files[0];

    if (file) {

        handleFile(file);

    }

});


/* =========================
   HANDLE FILE
========================= */

function handleFile(file) {

    const allowedTypes = [
        "image/jpeg",
        "image/png",
        "image/webp"
    ];


    if (!allowedTypes.includes(file.type)) {

        alert(
            "Please select a JPG, PNG or WEBP image."
        );

        return;

    }


    selectedFile = file;

    fileName.textContent = file.name;


    const reader = new FileReader();


    reader.onload = (event) => {

        imagePreview.src =
            event.target.result;

    };


    reader.readAsDataURL(file);


    previewContainer.classList.remove("hidden");

    analyzeButton.classList.remove("hidden");

    results.classList.add("hidden");

}


/* =========================
   REMOVE IMAGE
========================= */

removeButton.addEventListener("click", () => {

    selectedFile = null;

    fileInput.value = "";

    imagePreview.src = "";

    previewContainer.classList.add("hidden");

    analyzeButton.classList.add("hidden");

    results.classList.add("hidden");

});


/* =========================
   ANALYZE IMAGE
========================= */

analyzeButton.addEventListener("click", async () => {

    if (!selectedFile) {

        return;

    }


    const formData = new FormData();

    formData.append("file", selectedFile);


    analyzeButton.classList.add("hidden");

    loading.classList.remove("hidden");

    results.classList.add("hidden");


    try {

        const response = await fetch(
            "/analyze",
            {
                method: "POST",
                body: formData
            }
        );


        if (!response.ok) {

            throw new Error(
                `Server returned ${response.status}`
            );

        }


        const data = await response.json();


        if (!data.success) {

            alert(
                data.error ||
                "Image analysis failed."
            );

            return;

        }


        displayResults(data.predictions);


    }

    catch (error) {

        console.error(error);

        alert(
            "Unable to connect to the AI backend."
        );

    }

    finally {

        loading.classList.add("hidden");

        analyzeButton.classList.remove("hidden");

    }

});


/* =========================
   DISPLAY RESULTS
========================= */

function displayResults(predictions) {

    predictionList.innerHTML = "";


    predictions.forEach((prediction) => {

        const item =
            document.createElement("div");


        item.className = "prediction";


        item.innerHTML = `

            <div class="prediction-top">

                <span class="label">
                    ${prediction.label}
                </span>

                <span class="confidence">
                    ${prediction.confidence}%
                </span>

            </div>


            <div class="progress">

                <div
                    class="progress-bar"
                    style="width: ${prediction.confidence}%">
                </div>

            </div>

        `;


        predictionList.appendChild(item);

    });


    results.classList.remove("hidden");


    results.scrollIntoView({
        behavior: "smooth"
    });

}