import * as sqlite from "sqlite";

export const fetchData = async () => {
  try {
    const db = await sqlite.open('/Users/mariusaffolter/Documents/GitHub/sp_project_janosh_marius/backend_sp_db/Database/project_SP.db');
    console.log('Database opened');
    const result = await db.all('SELECT * FROM SP_Project_Sums');
    await db.close();
    return result;
  } catch (error) {
    console.error(error);
    return [];
  }
};