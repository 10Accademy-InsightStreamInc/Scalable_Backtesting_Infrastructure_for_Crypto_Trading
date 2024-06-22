// import PropTypes from "prop-types";

// const ResultData = ({ className = "" }) => {
//   return (
//     <div
//       className={`self-stretch flex flex-col items-start justify-start gap-[24px] max-w-full text-left text-5xl text-light-theme-text-primary-body font-subtitle-1 ${className}`}
//     >
//       <div className="self-stretch flex flex-col items-start justify-start gap-[28px] max-w-full text-13xl">
//         <div className="self-stretch flex flex-row items-start justify-between max-w-full gap-[20px] mq675:flex-wrap">
//           <div className="flex flex-col items-start justify-start pt-px px-0 pb-0">
//             <div className="flex flex-row items-start justify-start gap-[8px]">
//               <img
//                 className="h-10 w-10 relative rounded-sm overflow-hidden shrink-0 object-cover min-h-[40px]"
//                 loading="lazy"
//                 alt=""
//                 src="/avatar@2x.png"
//               />
//               <a className="[text-decoration:none] relative leading-[40px] font-semibold text-[inherit] mq450:text-lgi mq450:leading-[24px] mq900:text-7xl mq900:leading-[32px]">
//                 John Johnson
//               </a>
//             </div>
//           </div>
//           <div className="w-[328px] flex flex-row items-start justify-start gap-[16px] max-w-full text-base">
//             {/* User profile and notification */}
//           </div>
//         </div>
//         <div className="self-stretch h-px relative rounded-31xl bg-light-theme-border-and-divider-border-and-divider overflow-hidden shrink-0" />
//       </div>
//       <div className="self-stretch flex flex-col items-start justify-start gap-[24px] max-w-full">
//         <div className="self-stretch flex flex-col items-start justify-start gap-[16px] max-w-full">
//           <h3 className="m-0 relative text-inherit leading-[32px] font-medium font-inherit mq450:text-lgi mq450:leading-[26px]">
//             Backtest Results
//           </h3>
//           <div className="self-stretch flex flex-row flex-wrap items-start justify-start gap-[48px] max-w-full mq675:gap-[24px]">
//             <div className="flex-1 flex flex-col items-start justify-start gap-[16px] min-w-[372px] max-w-full mq450:min-w-full">
//               <div className="self-stretch flex flex-col items-start justify-start gap-[16px] max-w-full">
//                 <div className="flex flex-col items-start justify-start gap-[8px]">
//                   <h4 className="m-0 relative text-inherit leading-[28px] font-medium font-inherit mq450:text-lg mq450:leading-[24px]">
//                     Number of Trades
//                   </h4>
//                   <div className="relative text-base tracking-[0.2px] leading-[20px]">
//                     100
//                   </div>
//                 </div>
//                 <div className="flex flex-col items-start justify-start gap-[8px]">
//                   <h4 className="m-0 relative text-inherit leading-[28px] font-medium font-inherit mq450:text-lg mq450:leading-[24px]">
//                     Winning Trades
//                   </h4>
//                   <div className="relative text-base tracking-[0.2px] leading-[20px]">
//                     70
//                   </div>
//                 </div>
                
//                   <div className="flex flex-col items-start justify-start gap-[8px]">
//   <h4 className="m-0 relative text-inherit leading-[28px] font-medium font-inherit mq450:text-lg mq450:leading-[24px]">
//     Losing Trades
//   </h4>
//   <div className="relative text-base tracking-[0.2px] leading-[20px]">
//     30
//   </div>
// </div>
// <div className="flex flex-col items-start justify-start gap-[8px]">
//   <h4 className="m-0 relative text-inherit leading-[28px] font-medium font-inherit mq450:text-lg mq450:leading-[24px]">
//     Max Drawdown
//   </h4>
//   <div className="relative text-base tracking-[0.2px] leading-[20px]">
//     15%
//   </div>
// </div>
// <div className="flex flex-col items-start justify-start gap-[8px]">
//   <h4 className="m-0 relative text-inherit leading-[28px] font-medium font-inherit mq450:text-lg mq450:leading-[24px]">
//     Sharpe Ratio
//   </h4>
//   <div className="relative text-base tracking-[0.2px] leading-[20px]">
//     0.8
//   </div>
// </div>
//   </div>
// </div>
// </div>
// </div>
// </div>
// </div>
// );
// };

// ResultData.propTypes = {
//   className: PropTypes.string,
// };

// export default ResultData;

import PropTypes from "prop-types";

const ResultData = ({ className = "" }) => {
  return (
    <div
      className={`self-stretch flex flex-col items-start justify-start gap-[24px] max-w-full text-left text-5xl text-light-theme-text-primary-body font-subtitle-1 ${className}`}
    >
      <div className="self-stretch flex flex-col items-start justify-start gap-[28px] max-w-full text-13xl">
        <div className="self-stretch flex flex-row items-start justify-between max-w-full gap-[20px] mq675:flex-wrap">
          <div className="flex flex-col items-start justify-start pt-px px-0 pb-0">
            <div className="flex flex-row items-start justify-start gap-[8px]">
              <img
                className="h-10 w-10 relative rounded-sm overflow-hidden shrink-0 object-cover min-h-[40px]"
                loading="lazy"
                alt=""
                src="/avatar@2x.png"
              />
              <a className="[text-decoration:none] relative leading-[40px] font-semibold text-[inherit] mq450:text-lgi mq450:leading-[24px] mq900:text-7xl mq900:leading-[32px]">
                John Johnson
              </a>
            </div>
          </div>
          <div className="w-[328px] flex flex-row items-start justify-start gap-[16px] max-w-full text-base">
            {/* User profile and notification */}
          </div>
        </div>
        <div className="self-stretch h-px relative rounded-31xl bg-light-theme-border-and-divider-border-and-divider overflow-hidden shrink-0" />
      </div>
      <div className="self-stretch flex flex-col items-start justify-start gap-[24px] max-w-full">
        <div className="self-stretch flex flex-col items-start justify-start gap-[16px] max-w-full">
          <h3 className="m-0 relative text-inherit leading-[32px] font-medium font-inherit mq450:text-lgi mq450:leading-[26px]">
            Backtest Results
          </h3>
          <div className="self-stretch flex flex-row flex-wrap items-start justify-start gap-[48px] max-w-full mq675:gap-[24px]">
            <div className="flex-1 flex flex-col items-start justify-start gap-[16px] min-w-[372px] max-w-full mq450:min-w-full">
              <div className="self-stretch flex flex-col items-start justify-start gap-[16px] max-w-full">
                <div className="self-stretch rounded-md bg-light-theme-background-surfaces p-4 flex flex-col items-start justify-start gap-[8px]">
                  <h4 className="m-0 relative text-inherit leading-[28px] font-medium font-inherit mq450:text-lg mq450:leading-[24px]">
                    Number of Trades
                  </h4>
                  <div className="relative text-base tracking-[0.2px] leading-[20px]">
                    100
                  </div>
                </div>
                <div className="self-stretch rounded-md bg-light-theme-background-surfaces p-4 flex flex-col items-start justify-start gap-[8px]">
                  <h4 className="m-0 relative text-inherit leading-[28px] font-medium font-inherit mq450:text-lg mq450:leading-[24px]">
                    Winning Trades
                  </h4>
                  <div className="relative text-base tracking-[0.2px] leading-[20px]"></div>
                  </div>
</div>
<div className="self-stretch rounded-md bg-light-theme-background-surfaces p-4 flex flex-col items-start justify-start gap-[8px]">
  <h4 className="m-0 relative text-inherit leading-[28px] font-medium font-inherit mq450:text-lg mq450:leading-[24px]">
    Losing Trades
  </h4>
  <div className="relative text-base tracking-[0.2px] leading-[20px]">
    30
  </div>
</div>
<div className="self-stretch rounded-md bg-light-theme-background-surfaces p-4 flex flex-col items-start justify-start gap-[8px]">
  <h4 className="m-0 relative text-inherit leading-[28px] font-medium font-inherit mq450:text-lg mq450:leading-[24px]">
    Max Drawdown
  </h4>
  <div className="relative text-base tracking-[0.2px] leading-[20px]">
    15%
  </div>
</div>
<div className="self-stretch rounded-md bg-light-theme-background-surfaces p-4 flex flex-col items-start justify-start gap-[8px]">
  <h4 className="m-0 relative text-inherit leading-[28px] font-medium font-inherit mq450:text-lg mq450:leading-[24px]">
    Sharpe Ratio
  </h4>
  <div className="relative text-base tracking-[0.2px] leading-[20px]">
    0.8
  </div>
</div>
</div>
</div>
</div>
</div>
</div>
);
};

ResultData.propTypes = {
  className: PropTypes.string,
};

export default ResultData;