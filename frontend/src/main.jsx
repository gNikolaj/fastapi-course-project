import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';

import { Auth0Provider } from '@auth0/auth0-react';
import { ChakraProvider, defaultSystem } from '@chakra-ui/react';

import App from './App.jsx';

import { config } from './config.js';

import { ROUTES } from './constants/index.js';

import './index.css';

createRoot(document.getElementById('root')).render(
    <StrictMode>
        <ChakraProvider value={defaultSystem}>
            <Auth0Provider
                domain={config.auth0Domain}
                clientId={config.auth0ClientId}
                authorizationParams={{
                    redirect_uri: `${window.location.origin}${ROUTES.CALLBACK}`,
                    audience: config.auth0Audience,
                }}
            >
                <App />
            </Auth0Provider>
        </ChakraProvider>
    </StrictMode>,
);
