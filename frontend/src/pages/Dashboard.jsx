import { useEffect, useState } from 'react';

import { Box, Card, Heading, Spinner, Stack, Text } from '@chakra-ui/react';

import apiFetch from '../api/client.js';

import { API_ENDPOINTS, MESSAGES } from '../constants/index.js';

const Dashboard = () => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        apiFetch(API_ENDPOINTS.ME).then((data) => {
            setUser(data);
            setLoading(false);
        });
    }, []);

    if (loading) {
        return (
            <Box minH="100vh" display="flex" alignItems="center" justifyContent="center">
                <Spinner size="xl" />
            </Box>
        );
    }

    return (
        <Box minH="100vh" display="flex" alignItems="center" justifyContent="center" bg="bg.subtle">
            <Card.Root width="380px">
                <Card.Header>
                    <Heading size="lg">{MESSAGES.dashboard.title}</Heading>
                </Card.Header>
                <Card.Body>
                    <Stack gap={3}>
                        <Text>
                            <Text as="span" fontWeight="500">
                                {MESSAGES.dashboard.idLabel}
                            </Text>{' '}
                            {user?.id}
                        </Text>
                        <Text>
                            <Text as="span" fontWeight="500">
                                {MESSAGES.dashboard.emailLabel}
                            </Text>{' '}
                            {user?.email}
                        </Text>
                    </Stack>
                </Card.Body>
            </Card.Root>
        </Box>
    );
};

export default Dashboard;
