// import ResultData from "../components/ResultData";

// const Result = () => {
//   return (
//     <div className="w-full relative bg-light-theme-background-bg overflow-hidden flex flex-row items-start justify-start py-0 pr-8 pl-0 box-border gap-[32px] leading-[normal] tracking-[normal] text-left text-13xl text-light-theme-text-primary-body font-subtitle-1 mq900:gap-[16px] mq900:pl-5 mq900:box-border">
//       <div className="h-[982px] w-[253px] bg-light-theme-background-surfaces overflow-hidden shrink-0 flex flex-col items-start justify-between p-3 box-border mq900:hidden">
//         {/* Sidebar content */}
//       </div>
//       <section className="flex-1 flex flex-col items-start justify-start pt-10 px-0 pb-0 box-border max-w-[calc(100%_-_285px)] text-center text-base text-wireframe-100 font-subtitle-1 mq900:max-w-full">
//         <div className="self-stretch flex flex-col items-end justify-start gap-[43px] max-w-full mq675:gap-[21px]">
//           <ResultData />
//         </div>
//       </section>
//     </div>
//   );
// };

// export default Result;

import ResultData from "../components/ResultData";

const Result = () => {
  return (
    <div className="w-full relative bg-light-theme-background-bg overflow-hidden flex flex-row items-start justify-start py-0 pr-8 pl-0 box-border gap-[32px] leading-[normal] tracking-[normal] text-left text-13xl text-light-theme-text-primary-body font-subtitle-1 mq900:gap-[16px] mq900:pl-5 mq900:box-border">
      <div className="h-[982px] w-[253px] bg-light-theme-background-surfaces overflow-hidden shrink-0 flex flex-col items-start justify-between p-3 box-border mq900:hidden">
        <div className="self-stretch flex-1 flex flex-col items-start justify-start gap-[24px]">
          <div className="self-stretch flex flex-col items-start justify-center py-2 px-0">
            <div className="flex flex-row items-center justify-start">
              <a className="[text-decoration:none] relative leading-[32px] font-medium text-[inherit] inline-block min-w-[86px] mq450:text-lgi mq450:leading-[19px] mq900:text-7xl mq900:leading-[26px]">
                MELA
              </a>
            </div>
          </div>
          {/* Sidebar content */}
        </div>
        {/* Sidebar content */}
      </div>
      <section className="flex-1 flex flex-col items-start justify-start pt-10 px-0 pb-0 box-border max-w-[calc(100%_-_285px)] text-center text-base text-wireframe-100 font-subtitle-1 mq900:max-w-full">
        <div className="self-stretch flex flex-col items-end justify-start gap-[43px] max-w-full mq675:gap-[21px]">
          <ResultData />
        </div>
      </section>
    </div>
  );
};

export default Result;