const { VITE_AUTH0_DOMAIN, VITE_AUTH0_CLIENT_ID, VITE_AUTH0_AUDIENCE, VITE_API_URL } = import.meta.env;

export const config = {
    apiUrl: VITE_API_URL,
    auth0Domain: VITE_AUTH0_DOMAIN,
    auth0Audience: VITE_AUTH0_AUDIENCE,
    auth0ClientId: VITE_AUTH0_CLIENT_ID,
};
