import request from "./utils/request";

export const user = {
    user: () => {
        return request('GET', 'user');
    },
    users: (team = "", user = "", role = "", sortBy = "created", sortByType = "desc", page = 1, isModal = 0) => {
        return request('GET', `users?id_apm_team=${team}&name=${user}&id_acl_role=${role}&sort_by=${sortBy}&sort_by_type=${sortByType}&page=${page}&goal_modal=${isModal}`);
    },
    addUser: (data) => {
        return request('POST', 'users', data);
    },
    editUser: (id, data) => {
        return request('PUT', `users/${id}`, data);
    },
    deleteUser: (id, page = 1) => {
        return request('DELETE', `users/${id}?page=${page}`);
    },
    getUserByID: (userID, permissionDenied = '') => {
        return request('GET', `users/${userID}?permission_denied=${permissionDenied}`);
    },
    getSpecificUserActivity: (id, page = 1, permissionDenied = '') => {
        return request("GET", `users/${id}/activity?page=${page}&permission_denied=${permissionDenied}`);
    },
    addPostForSpecificUser: (id, data, permissionDenied) => {
        return request("POST", `users/${id}/post?permission_denied=${permissionDenied}`, data);
    },
    getPostForSpecificUser: (id, page = 1, permissionDenied = '') => {
        return request("GET", `users/${id}/posts?page=${page}&permission_denied=${permissionDenied}`);
    },
    deleteSpecificUserPost: (postId) => {
        return request("DELETE", `users/post/${postId}`);
    },
    editSpecificUserPost: (postId, data) => {
        return request("PUT", `users/post/${postId}`, data);
    },
};
