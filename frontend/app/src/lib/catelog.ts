export type product = {
  name:string,
  description: string,
  category: number,
  active: boolean
}

type productResult = {
  count: number,
  next: string,
  previous: string,
  results: product[]
}

export async function productList(): Promise<productResult> {
  const response = await fetch(
    `${import.meta.env.VITE_API_PATH}/catelog/products/`
  );
  const result = await response.json();
  if(result) {
    result.results.sort((itemA:product, itemB:product) => {
      return itemA.name.localeCompare(itemB.name)
    })
  }

  return result;
} 
