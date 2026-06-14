import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import { Box, Button, Card, Field, Heading, Input, Stack, Text } from '@chakra-ui/react';

import apiFetch from '../api/client.js';

import { ROUTES, API_ENDPOINTS, MESSAGES } from '../constants/index.js';

const RegisterPage = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const navigate = useNavigate();

    const handleRegister = async () => {
        setError(null);
        setLoading(true);

        try {
            await apiFetch(API_ENDPOINTS.REGISTER, {
                method: 'POST',
                body: JSON.stringify({ email, password }),
            });

            navigate(ROUTES.LOGIN, { replace: true });
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
                    <Heading size="lg">{MESSAGES.register.title}</Heading>
                    <Text color="fg.muted" fontSize="sm">
                        {MESSAGES.register.haveAccount}{' '}
                        <Text as="span" color="blue.500" cursor="pointer" onClick={() => navigate(ROUTES.LOGIN)}>
                            {MESSAGES.register.signInLink}
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

                        <Button width="full" loading={loading} onClick={handleRegister}>
                            {MESSAGES.register.submit}
                        </Button>
                    </Stack>
                </Card.Body>
            </Card.Root>
        </Box>
    );
};

export default RegisterPage;
