export async function appList() {
  const response = await fetch(
    `${import.meta.env.VITE_API_PATH}/config/apps/`
  );
  const results = await response.json();

  return results;
} 

export async function companyName() {
  const response = await fetch(
    `${import.meta.env.VITE_API_PATH}/config/company/`
  );
  const results = await response.json();

  return results;
}