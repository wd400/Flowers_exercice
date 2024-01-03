export const environment = {
    maxPage:  parseInt('${ENV_BACKEND_URI}' as string || '10'),
    apiUrl: 'http://api:5000'
  };