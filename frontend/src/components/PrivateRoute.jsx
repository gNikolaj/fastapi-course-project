import { Navigate, Outlet } from 'react-router-dom';

import { ROUTES, STORAGE_KEYS } from '../constants/index.js';

const PrivateRoute = () => {
    const token = localStorage.getItem(STORAGE_KEYS.TOKEN);
    return token ? <Outlet /> : <Navigate to={ROUTES.LOGIN} replace />;
};

export default PrivateRoute;
