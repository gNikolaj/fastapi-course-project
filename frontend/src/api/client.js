import { config } from '../config.js';

import { ROUTES, STORAGE_KEYS, MESSAGES } from '../constants/index.js';

const apiFetch = async (path, options = {}) => {
    const token = localStorage.getItem(STORAGE_KEYS.TOKEN);

    const res = await fetch(`${config.apiUrl}${path}`, {
        ...options,
        headers: {
            'Content-Type': 'application/json',
            ...(token ? { Authorization: `Bearer ${token}` } : {}),
            ...options.headers,
        },
    });

    const data = await res.json();

    if (res.status === 401) {
        localStorage.removeItem(STORAGE_KEYS.TOKEN);
        window.location.href = ROUTES.LOGIN;
        return null;
    }

    if (!res.ok) {
        throw new Error(data.detail || MESSAGES.common.genericError);
    }

    return data;
};

export default apiFetch;
