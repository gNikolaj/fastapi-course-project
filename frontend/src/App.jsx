import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';

import LoginPage from './pages/LoginPage.jsx';
import Dashboard from './pages/Dashboard.jsx';
import AuthCallback from './pages/AuthCallback.jsx';
import RegisterPage from './pages/RegisterPage.jsx';
import PrivateRoute from './components/PrivateRoute.jsx';

import { ROUTES } from './constants/index.js';

const App = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path={ROUTES.HOME} element={<Navigate to={ROUTES.LOGIN} replace />} />
                <Route path={ROUTES.LOGIN} element={<LoginPage />} />
                <Route path={ROUTES.CALLBACK} element={<AuthCallback />} />
                <Route path={ROUTES.REGISTER} element={<RegisterPage />} />

                <Route element={<PrivateRoute />}>
                    <Route path={ROUTES.DASHBOARD} element={<Dashboard />} />
                </Route>
            </Routes>
        </BrowserRouter>
    );
};

export default App;
