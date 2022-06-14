import axios from 'axios';
import useNotification from "@hooks/useNotification";

export default function request(method, url, data) {
    const errorNote = useNotification;
    const token = localStorage.getItem("auth_token");
    const apiUrl = process.env.valueOf().REACT_APP_API_URL;

    return axios({
        method: method,
        url: apiUrl + url,
        headers: {
            'Authorization': `Bearer ${token}`
        },
        data: data
    }).then((response) => {
        return response;
    }).catch((error) => {
        if (error?.response?.status === 300) {
            console.log(error.response);
            throw error;
        }

        if (error.response && error.response.data.message === 'Unauthenticated.') {
            localStorage.removeItem("auth_token");
            window.location.href = '/apm/login';
        } else {
            let errorMessage;

            if(typeof error.response?.data?.error_message !== 'object') {
                errorMessage = error.response?.data?.error_message ?? error.response?.data?.message;
            } else {
                errorMessage = Object
                    .keys(error.response.data.error_message)
                    .map(key => error.response.data.error_message[key]).join(' ');
            }

            errorNote(
                "error",
                "Warning!",
                errorMessage
            )
            console.log((error.response && error?.response?.data?.errors?.name) || error?.response?.data?.message, "Error");
        }
    });
}