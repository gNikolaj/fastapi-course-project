import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import { useAuth0 } from '@auth0/auth0-react';

import { ROUTES, STORAGE_KEYS, MESSAGES } from '../constants/index.js';

const AuthCallback = () => {
    const navigate = useNavigate();
    const { getAccessTokenSilently, isAuthenticated, isLoading } = useAuth0();

    useEffect(() => {
        if (isLoading || !isAuthenticated) return;

        (async () => {
            const token = await getAccessTokenSilently();
            localStorage.setItem(STORAGE_KEYS.TOKEN, token);
            navigate(ROUTES.DASHBOARD, { replace: true });
        })();
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [isAuthenticated, isLoading]);

    return <p>{MESSAGES.common.loading}</p>;
};

export default AuthCallback;
