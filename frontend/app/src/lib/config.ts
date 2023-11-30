export async function appList() {
  const response = await fetch(
    `http://192.168.88.244:8000/api/v1/config/apps/`
  );
  const results = await response.json();

  return results;
} 

export async function companyName() {
  const response = await fetch(
    `http://192.168.88.244:8000/api/v1/config/company/`
  );
  const results = await response.json();

  return results;
}