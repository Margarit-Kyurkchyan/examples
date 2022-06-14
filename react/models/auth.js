import request from "./utils/request";

export const auth = {
    sendResetPasswordLink: (email) => {
        return request('POST', 'password/email', {email});
    },
    resetPassword: (data) => {
        return request('POST', 'password/reset', data);
    },
};