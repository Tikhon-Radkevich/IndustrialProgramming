async function uploadFile() {
    const fileOption = document.getElementById("fileOption").value;
    const fileInput = document.getElementById("file").files[0];
    const textInput = document.getElementById("keyInput").value;
    const useCustomLibsCheckbox = document.getElementById("useCustomLibs");
    const useCustomLibsValue = useCustomLibsCheckbox.checked;

    const formData = new FormData();
    formData.append("file_option", fileOption);
    formData.append("file", fileInput);
    formData.append("key", textInput);
    formData.append("use_custom_libs", useCustomLibsValue);

    const response = await fetch("/uploadfile/", {
        method: "POST",
        body: formData
    });
    const result = await response.json();

    console.log(result.message);

    document.getElementById("messageDiv").innerText = result.message;
    window.expressionsData = result.expressions_data;
}

async function downloadFile() {
    const fileOption = document.getElementById("saveFileOption").value;
    const fileFormat = document.getElementById("fileFormat").value;
    const fileName = document.getElementById("fileName").value;
    const useCustomLibsCheckbox = document.getElementById("useCustomLibs");
    const useCustomLibsValue = useCustomLibsCheckbox.checked;

    const formData = new FormData();
    formData.append("file_option", fileOption);
    formData.append("file_name", fileName);
    formData.append("file_format", fileFormat);
    formData.append("expressions_data", JSON.stringify(window.expressionsData));
    formData.append("use_custom_libs", useCustomLibsValue);

    const response = await fetch("/download/", {
        method: "POST",
        body: formData
    });
    if (response.ok) {
        const contentDisposition = response.headers.get('Content-Disposition');
        const filenameMatch = contentDisposition && contentDisposition.match(/filename="(.+?)"/);
        const filename = filenameMatch ? filenameMatch[1] : 'downloaded-file';

        const blob = await response.blob();

        const link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob);
        link.download = filename;

        document.body.appendChild(link);
        link.click();

        document.body.removeChild(link);
    } else {
        console.error("Download failed:", response.statusText);
    }
}
