import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import { useAuth0 } from '@auth0/auth0-react';
import { Box, Button, Card, Field, Heading, Input, Separator, Stack, Text } from '@chakra-ui/react';

import apiFetch from '../api/client.js';

import { ROUTES, API_ENDPOINTS, STORAGE_KEYS, AUTH_CONNECTIONS, MESSAGES } from '../constants/index.js';

const LoginPage = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const navigate = useNavigate();
    const { loginWithRedirect } = useAuth0();

    const handleLocalLogin = async () => {
        setError(null);
        setLoading(true);

        try {
            const data = await apiFetch(API_ENDPOINTS.LOGIN, {
                method: 'POST',
                body: JSON.stringify({ email, password }),
            });

            if (!data) return;

            localStorage.setItem(STORAGE_KEYS.TOKEN, data.access_token);
            navigate(ROUTES.DASHBOARD, { replace: true });
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <Box minH="100vh" display="flex" alignItems="center" justifyContent="center" bg="bg.subtle">
            <Card.Root width="380px">
                <Card.Header>
                    <Heading size="lg">{MESSAGES.login.title}</Heading>
                    <Text color="fg.muted" fontSize="sm">
                        {MESSAGES.login.noAccount}{' '}
                        <Text as="span" color="blue.500" cursor="pointer" onClick={() => navigate(ROUTES.REGISTER)}>
                            {MESSAGES.login.signUpLink}
                        </Text>
                    </Text>
                </Card.Header>

                <Card.Body>
                    <Stack gap={4}>
                        <Field.Root invalid={!!error}>
                            <Field.Label>{MESSAGES.common.emailLabel}</Field.Label>
                            <Input
                                type="email"
                                placeholder={MESSAGES.common.emailPlaceholder}
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                            />
                        </Field.Root>

                        <Field.Root invalid={!!error}>
                            <Field.Label>{MESSAGES.common.passwordLabel}</Field.Label>
                            <Input
                                type="password"
                                placeholder={MESSAGES.common.passwordPlaceholder}
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                            />
                            {error && <Field.ErrorText>{error}</Field.ErrorText>}
                        </Field.Root>

                        <Button width="full" loading={loading} onClick={handleLocalLogin}>
                            {MESSAGES.login.submit}
                        </Button>

                        <Separator />

                        <Button
                            width="full"
                            variant="outline"
                            onClick={() =>
                                loginWithRedirect({ authorizationParams: { connection: AUTH_CONNECTIONS.GOOGLE } })
                            }
                        >
                            {MESSAGES.login.google}
                        </Button>

                        <Button
                            width="full"
                            variant="outline"
                            onClick={() =>
                                loginWithRedirect({ authorizationParams: { connection: AUTH_CONNECTIONS.GITHUB } })
                            }
                        >
                            {MESSAGES.login.github}
                        </Button>
                    </Stack>
                </Card.Body>
            </Card.Root>
        </Box>
    );
};

export default LoginPage;
