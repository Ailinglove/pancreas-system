import axios from 'axios';

//对病人基本信息进行数据交互
export const getPatientList = params => { return axios.get("/api/retPatientList/", { params: params }); };
export const upgradePatient=params => { return axios.get("/api/patient/upgrade/", { params: params }); };
// export const removePancreas = params => {return axios.get(`/api/pancreas/remove`, { params: params }); };

//对胰腺数据进行数据交互
export const getPancreasList = params => { return axios.get("/api/ret_pancreasinfolist/", { params: params }); };
export const upgradeImgData=params => { return axios.get("/api/pancreas/upgrade/", { params: params }); };
export const removePancreas = params => {return axios.get(`/api/pancreas/remove`, { params: params }); };

//对用户信息进行交互
export const edituser=params => { return axios.get("/api/user/edit", { params: params }); };
export const removeUsers = params => {return axios.get(`/api/user/remove`, { params: params }); };
//病理数据交互
export const getPathoInfoList = params => { return axios.get("/api/retPathoInfoList/", { params: params }); };
export const upgradePathoData = params => { return axios.get("/api/pathoData/upgrade/", { params: params }); };

// 肿瘤标志物数据交互
export const getTumorMarkerList = params => { return axios.get("/api/retTumorMarkerInfoList/", { params: params }); };


//获取图像数据url
export const getImgURL = params => { return axios.get("/api/getImgURL/", { params: params }); };
