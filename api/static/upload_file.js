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
