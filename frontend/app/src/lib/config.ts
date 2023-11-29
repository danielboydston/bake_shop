export async function appList() {
  const response = await fetch(
    `http://localhost:8000/api/v1/config/apps/`
  );
  const results = await response.json();

  return results;
}